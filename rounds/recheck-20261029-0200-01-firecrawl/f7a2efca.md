[Sitemap](https://dshills.medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fdshills.medium.com%2Fbuilding-an-mcp-server-from-scratch-432f700b5e68&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-------------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav--------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fdshills.medium.com%2Fbuilding-an-mcp-server-from-scratch-432f700b5e68&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

[AI](https://medium.com/tag/ai?source=post_page---header_tags--432f700b5e68-----------------------------------------)

[Go](https://medium.com/tag/go?source=post_page---header_tags--432f700b5e68-----------------------------------------)

[Mcp Server](https://medium.com/tag/mcp-server?source=post_page---header_tags--432f700b5e68-----------------------------------------)

[Mcp Protocol](https://medium.com/tag/mcp-protocol?source=post_page---header_tags--432f700b5e68-----------------------------------------)

[Gpt](https://medium.com/tag/gpt?source=post_page---header_tags--432f700b5e68-----------------------------------------)

# Building an MCP Server from Scratch (with a Little Help from GPT)

[![Davin Hills](https://miro.medium.com/v2/resize:fill:32:32/0*oxmaeynlEvTxLX92.jpg)](https://dshills.medium.com/?source=post_page---byline--432f700b5e68-----------------------------------------)

[Davin Hills](https://dshills.medium.com/?source=post_page---byline--432f700b5e68-----------------------------------------)

Follow

4 min read

·

Apr 22, 2025

58

3

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D432f700b5e68&operation=register&redirect=https%3A%2F%2Fdshills.medium.com%2Fbuilding-an-mcp-server-from-scratch-432f700b5e68&source=---header_actions--432f700b5e68---------------------post_audio_button--------------------)

Share

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*nNz-h-6YQSFZyauPGF5K6Q.png)

When I first set out to build an MCP server — short for **Model Context Protocol** — I wasn’t just chasing a new framework. I was chasing understanding.

I’ve found that _the best way to truly understand a system is to build it yourself._ And LLM orchestration — chaining tools, injecting context, retrieving memory, running prompts — is no exception. There are frameworks like LangChain and Semantic Kernel, but I wanted to see how it all actually works under the hood.

This article walks through how I built my own MCP server — what it does, how I structured it, and how GPT helped clarify architecture without ever taking the wheel.

## 🧠 What Is an MCP Server?

The goal of an MCP server is to abstract over common LLM-driven workflows:

- Prompt execution with variable injection
- Session tracking and context persistence
- Calling tools (shell commands, APIs, or internal functions)
- Searching memory — both vector and structured
- Switching LLMs on demand (OpenAI, Claude, Ollama)

All via a clean JSON protocol that can be sent over HTTP or stdin/stdout.

In short, it’s _middleware for building intelligent, contextual LLM applications._

## 🔧 Why I Built It From Scratch

The main reason? **To learn.** I wanted to deeply understand how these systems are wired together.

Rather than use a full-stack orchestration framework and fill in blanks, I wanted to _fill in the architecture_ — how prompt templates are resolved, how tools are tracked, how memory integrates into workflows, and how async jobs should behave.

## Get Davin Hills’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

Along the way I built something lightweight, Go-native, dependency-minimal, and extensible. Here’s how.

## 🧱 Core Architecture

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*zFY_59Bn-PhQ28Yx9eApCg.png)

## 📦 Protocol Overview

Each request looks like this:

```
{
  "id": "req-001",
  "method": "runPrompt",
  "params": {
    "prompt": "summarize",
    "input": "This is a long passage..."
  }
}
```

Each method is dispatched to a handler registered in a map:

```
type methodHandler func(*Server, mcp.Request) mcp.Response
```

```
var handlers = map[string]methodHandler{
	"runPrompt":      (*Server).handleRunPrompt,
	"callTool":       (*Server).handleCallTool,
	"callToolAsync":  (*Server).handleCallToolAsync,
	"getToolResult":  (*Server).handleGetToolResult,
	"getMemory":      (*Server).handleGetMemory,
	"searchMemory":   (*Server).handleSearchMemory,
}
```

## 🧩 Server Loop

For stdin mode (CLI), I use a loop that reads from a JSON decoder and dispatches asynchronously:

```
func (s *Server) Start() error {
	for {
		var req mcp.Request
		if err := s.dec.Decode(&req); err != nil {
			if err == io.EOF {
				time.Sleep(100 * time.Millisecond)
				continue
			}
			return fmt.Errorf("decode failed: %w", err)
		}
		go s.handle(req)
	}
}
```

HTTP mode uses the same dispatch pattern via POST /mcp.

## 🧠 Prompt Execution

Prompts are simple Go templates stored in a prompts/ directory:

```
prompts/
  summarize.txt
  classify_risk.txt
  answer_question.txt
```

Each prompt is rendered with context merged from:

- Input params
- Session memory
- Retrieved vector memory
- Tool outputs (if needed)

```
func (s *Server) handleRunPrompt(req mcp.Request) mcp.Response {
	params := req.Params.(map[string]any)
	name := params["prompt"].(string)
	data := extractTemplateVars(params)
	tmpl, err := s.prompts.Load(name)
	content := tmpl.Render(data)
```

```
	result, err := s.llmClient.Complete(ctx, content)
	...
}
```

## 🔌 Tool Execution

Tools are modular and registered at startup. They can be shell commands, Go functions, or remote APIs:

```
type Tool interface {
	Name() string
	Run(ctx context.Context, args []string) (ToolResult, error)
}
```

```
type ShellTool struct {
	Command string
}func (s ShellTool) Run(ctx context.Context, args []string) (ToolResult, error) {
	cmd := exec.CommandContext(ctx, s.Command, args...)
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	return ToolResult{Output: out.String()}, err
}
```

Async tool calls are stored with a UUID and status tracking in a simple in-memory map (or persistent DB):

```
toolID := uuid.New().String()
go func() {
	result, err := tool.Run(ctx, args)
	s.jobStore.Set(toolID, result, err)
}()
```

## 🧬 Memory + Embeddings

I wanted to support both relational (MySQL) and vector-based memory (Qdrant, Pinecone).

```
type MemoryStore interface {
	AddMemory(ctx context.Context, sessionID string, data MemoryItem) error
	Search(ctx context.Context, sessionID, query string, tags []string) ([]MemoryItem, error)
}
```

A vector implementation uses an embedding provider:

```
embedding := embedder.Embed(query)
results := qdrant.Search(embedding, tags)
```

Each memory item includes metadata, a timestamp, and an optional vector.

## 🤖 LLM Backend Switching

I abstracted LLM calls via a Model interface:

```
type Model interface {
	Complete(ctx context.Context, prompt string) (string, error)
}
```

With implementations for:

- OpenAI
- Claude
- Ollama (local)

The user can specify which model to use per call or per session.

## 🧭 GPT as a Design Partner

I didn’t ask GPT to build the system for me. I used it like a sounding board:

- “Should tool outputs be cached or re-executed?”
- “How does LangChain handle memory injection?”
- “Should I use UUIDs or hashes for job tracking?”

Its strength wasn’t codegen — it was architecture fluency. It helped me avoid rabbit holes and stay grounded in best practices while still owning every decision.

## 🔭 What’s Next

This isn’t done — it’s evolving:

- ✅ mcp-cli REPL with prompt preview and colorized output
- 🔄 Hot-swappable model selection (via request or config)
- 🧠 Role-based memory segmentation (persona/context tracking)
- 📊 Observability layer: structured logs, tracing, async metrics
- 🌐 Web dashboard for prompt and memory visibility

Eventually, I may turn this into an open plugin system, where new tools, models, and memory backends can register dynamically.

## 🧵 Final Thoughts

Building this server from scratch taught me more than any documents or libraries could. I now understand the shape of these systems—not just how to use them but how they work, where they break, and how to adapt them.

If you’re an engineer curious about LLM operations, _build your own MCP layer._ Use GPT as your rubber duck. You’ll walk away with a system that works _and_ a deep mental model of how everything connects.

And hey, you’ll probably have more fun doing it too.

[AI](https://medium.com/tag/ai?source=post_page---footer_tags--432f700b5e68-----------------------------------------)

[Go](https://medium.com/tag/go?source=post_page---footer_tags--432f700b5e68-----------------------------------------)

[Mcp Server](https://medium.com/tag/mcp-server?source=post_page---footer_tags--432f700b5e68-----------------------------------------)

[Mcp Protocol](https://medium.com/tag/mcp-protocol?source=post_page---footer_tags--432f700b5e68-----------------------------------------)

[Gpt](https://medium.com/tag/gpt?source=post_page---footer_tags--432f700b5e68-----------------------------------------)

[![Davin Hills](https://miro.medium.com/v2/resize:fill:48:48/0*oxmaeynlEvTxLX92.jpg)](https://dshills.medium.com/?source=post_page---post_author_info--432f700b5e68-----------------------------------------)

[![Davin Hills](https://miro.medium.com/v2/resize:fill:64:64/0*oxmaeynlEvTxLX92.jpg)](https://dshills.medium.com/?source=post_page---post_author_info--432f700b5e68-----------------------------------------)

Follow

[**Written by Davin Hills**](https://dshills.medium.com/?source=post_page---post_author_info--432f700b5e68-----------------------------------------)

[151 followers](https://dshills.medium.com/followers?source=post_page---post_author_info--432f700b5e68-----------------------------------------)

· [94 following](https://dshills.medium.com/following?source=post_page---post_author_info--432f700b5e68-----------------------------------------)

30+ years of experience in software engineering and architecture.

Follow

[Help](https://help.medium.com/hc/en-us?source=post_page-----432f700b5e68-----------------------------------------)

[Status](https://status.medium.com/?source=post_page-----432f700b5e68-----------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----432f700b5e68-----------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----432f700b5e68-----------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----432f700b5e68-----------------------------------------)

[Store](https://medium.com/store)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----432f700b5e68-----------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----432f700b5e68-----------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----432f700b5e68-----------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----432f700b5e68-----------------------------------------)