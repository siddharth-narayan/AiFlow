<script lang="ts">
    import AiMediaView from "$lib/components/ai-media-input.svelte";
    import MediaTypeSelector from "$lib/components/media-type-selector.svelte";
    import { Select } from "$lib/components/ui/select";
    import SelectContent from "$lib/components/ui/select/select-content.svelte";
    import SelectItem from "$lib/components/ui/select/select-item.svelte";

    import { Separator } from "$lib/components/ui/separator/index.js";
    
    let media_type_1 = $state("text")
    let media_type_2 = $state("text")

    function getAvailableModels(type: string, type1: string) {
        
    }
</script>

<div>
    <div class="flex justify-center">
        <Select>
            <SelectContent>
                <SelectItem value=""></SelectItem>
            </SelectContent>
        </Select>
    </div>
</div>
<div class="flex gap-4 p-4 h-full">
    <div class="w-1/2 flex flex-col gap-4 items-center">
        <MediaTypeSelector bind:value={media_type_1}></MediaTypeSelector>
        <AiMediaView type={media_type_1} interactive={true}/>
    </div>
    <Separator orientation="vertical" />
    <div class="w-1/2 flex flex-col gap-4 items-center">
        <MediaTypeSelector bind:value={media_type_2}></MediaTypeSelector>
        <AiMediaView type={media_type_1} interactive={false}/>
    </div>
</div>
