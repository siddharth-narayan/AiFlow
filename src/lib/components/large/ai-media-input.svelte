<script>
    import { Textarea } from "../ui/textarea";

    let { type } = $props();
    let value = $state("")
</script>

{#if type == "text"}
    <Textarea placeholder="Enter your message" bind:value></Textarea>
{:else if type == "audio"}{:else if type == "video"}{:else if type == "3D"}{/if}