from llm_client import LLMClient

def main():
    llm = LLMClient("http://localhost:11434/api", "qwen2.5-coder:7b-instruct")
    hir_command = "rustc +nightly -Z unpretty=hir file.rs"

    print(llm.send_message("<insert_template>"))


if __name__ == "__main__":
    main()