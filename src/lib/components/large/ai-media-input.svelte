<script>
    import { AutoTokenizer } from "@huggingface/transformers";
    import { Upload } from "@lucide/svelte"
    import { Textarea } from "../ui/textarea";
    import { Button } from "../ui/button";

    let { value = $bindable(), type } = $props();

</script>

{#if type == "text"}
    <Textarea placeholder="Enter your message" bind:value></Textarea>
{:else if type == "audio"}
    <Button>
        <Upload></Upload>
    </Button>
{:else if type == "video"}{:else if type == "3D"}{/if}
