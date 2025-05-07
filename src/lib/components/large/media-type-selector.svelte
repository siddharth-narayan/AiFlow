<script>
    import { Select, SelectGroup } from "$lib/components/ui/select";
    import SelectContent from "$lib/components/ui/select/select-content.svelte";
    import SelectItem from "$lib/components/ui/select/select-item.svelte";
    import SelectTrigger from "$lib/components/ui/select/select-trigger.svelte";
    
    let { value = $bindable() } = $props();
</script>

<div class="w-1/3 max-w-32">
    <Select type="single" bind:value>
        <SelectTrigger placeholder="Heloeawf">
            {value}
        </SelectTrigger>
        <SelectContent placeholder="Value">
            <SelectItem value="text"></SelectItem>
            <SelectItem value="audio"></SelectItem>
            <SelectItem value="video"></SelectItem>
            <SelectItem value="3D"></SelectItem>
        </SelectContent>
    </Select>
</div>