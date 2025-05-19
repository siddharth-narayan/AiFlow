<script>
    import { AutoTokenizer } from "@huggingface/transformers";
    import { Textarea } from "../ui/textarea";
    import { Button } from "../ui/button";

    let { type } = $props();
    let value = $state("");

    async function onclick() {
        console.log("Subbmittttt");
        let tokenizer = await AutoTokenizer.from_pretrained("Xenova/t5-base");
        const { input_ids } = await tokenizer(
            "Translate English to German: I love transformers!",
        );
        console.log(input_ids);

        encode_resp = fetch("https://test.novaphaze.com/t5-encode/infer", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                inputs: [
                    {
                        name: "input_ids",
                        shape: [1, input_ids.length],
                        datatype: "INT32",
                        data: input_ids,
                    },
                ],
                outputs: [{ name: "encoder_hidden_states" }],
            }),
        });
    }
</script>

{#if type == "text"}
    <Textarea placeholder="Enter your message" bind:value></Textarea>
    <Button {onclick}>Submitshs</Button>
{:else if type == "audio"}{:else if type == "video"}{:else if type == "3D"}{/if}
