<script lang="ts">
    import { Upload } from "@lucide/svelte";
    import { Textarea } from "../ui/textarea";
    import { Button } from "../ui/button";
    import type { DataType } from "$lib/api/triton/types";

    type Props = {
        value: any;
        type: {
            name: string;
            data_type: DataType;
        };
    };
    let { value = $bindable(), type }: Props = $props();

    console.log(type);
</script>

{#if type.data_type == "TYPE_STRING"}
    <Textarea placeholder="Enter your message" bind:value></Textarea>
{:else}
    <Button>
        <Upload></Upload>
    </Button>
{/if}
<!-- {:else if type == "audio"}
    <Button>
        <Upload></Upload>
    </Button>
{:else if type == "video"}{:else if type == "3D"}{/if} -->
