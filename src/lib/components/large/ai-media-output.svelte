<script>
    import { Card } from "../ui/card";
    import CardContent from "../ui/card/card-content.svelte";
    import { Textarea } from "../ui/textarea";

    let { type } = $props();
    let value = $state("")
</script>

{#if type == "text"}
        <Card class="w-full">
            <CardContent>

            </CardContent>
        </Card>
{:else if type == "audio"}{:else if type == "video"}{:else if type == "3D"}{/if}