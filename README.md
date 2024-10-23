# TRACTOR Macro-Refolding

Reimplementing the blog post (prompts borrowed from here too): https://galois.com/blog/2023/09/using-gpt-4-to-assist-in-c-to-rust-translation/

Currently using https://ollama.com/library/qwen2.5-coder:7b-instruct as the locally hosted LLM, set up steps here: https://github.com/ollama/ollama. From what I've read, this is one of the best coding models available for a relatively low parameter size (from Ollama: You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models). We should set up a larger LLM later.

TODOs:
- macro creation
- compile LLM-generated Rust and C2Rust code to HIR (https://rustc-dev-guide.rust-lang.org/hir.html)
- formatting HIRs and then performing equality check
- iteration for macro creation (https://github.com/GaloisInc/blog-saw-and-llms/blob/main/blog-c2rust-and-llms/creation_failure_example.txt)
- macro insertion steps
- testing and iteration
- containerization








