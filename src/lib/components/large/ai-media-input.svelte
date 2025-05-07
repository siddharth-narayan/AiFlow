<script>
    import { AutoTokenizer } from '@huggingface/transformers';
    import { Textarea } from "../ui/textarea";
    import { Button } from '../ui/button';

    let { type } = $props();
    let value = $state("")

    async function onclick() {
        console.log("Subbmittttt")
        let tokenizer = await AutoTokenizer.from_pretrained("google-t5/t5-base")
        const { input_ids } = await tokenizer('I love transformers!');
        console.log(input_ids)
    }
</script>

{#if type == "text"}
    <Textarea placeholder="Enter your message" bind:value></Textarea>
<<<<<<< HEAD
{:else if type == "audio"}{:else if type == "video"}{:else if type == "3D"}{/if}
=======
    <Button {onclick}>Submitshs</Button>
{:else if type == "audio"}{:else if type == "video"}{:else if type == "3D"}{/if}
>>>>>>> a4c32c5 (Misc)
