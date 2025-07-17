<script>
    import { AutoTokenizer } from "@huggingface/transformers";
    import { Textarea } from "../ui/textarea";
    import { Button } from "../ui/button";

    let { value = $bindable(), type } = $props();

</script>

{#if type == "text"}
    <Textarea placeholder="Enter your message" bind:value></Textarea>
{:else if type == "audio"}{:else if type == "video"}{:else if type == "3D"}{/if}
