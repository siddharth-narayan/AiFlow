<script lang="ts">
    import AiMediaInput from "$lib/components/large/ai-media-input.svelte";
    import AiMediaOutput from "$lib/components/large/ai-media-output.svelte";
    import SingleSelect from "$lib/components/large/single-select.svelte";

    import { Separator } from "$lib/components/ui/separator/index.js";
    
    let media_type_1 = $state("text")
    let media_type_2 = $state("text")

    let mediaTypes = ["audio", "video", "text", "3D"]
    function getAvailableModels(type: string, type1: string) {
        fetch()
    }
</script>

<div>
    <div class="flex justify-center">
        <p>models</p>
    </div>
</div>
<div class="flex gap-4 p-4 h-full">
    <div class="w-1/2 flex flex-col gap-4 items-center">
        <SingleSelect bind:value={media_type_1} options={mediaTypes}></SingleSelect>
        <AiMediaInput type={media_type_1}/>
    </div>
    <Separator orientation="vertical" />
    <div class="w-1/2 flex flex-col gap-4 items-center">
        <SingleSelect bind:value={media_type_2} options={mediaTypes}></SingleSelect>
        <AiMediaOutput type={media_type_1} interactive={false}/>
    </div>
</div>
