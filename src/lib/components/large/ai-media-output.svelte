<script>
    import { Card } from "../ui/card";
    import CardContent from "../ui/card/card-content.svelte";
    import { Textarea } from "../ui/textarea";

    let { value, type } = $props();
</script>

{#if type == "text"}
        <Card class="w-full">
            <CardContent>
                {value}
            </CardContent>
        </Card>
{:else if type == "audio"}{:else if type == "video"}{:else if type == "3D"}{/if}
