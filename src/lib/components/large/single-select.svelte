<script>
    import { Select, SelectGroup } from "$lib/components/ui/select";
    import SelectContent from "$lib/components/ui/select/select-content.svelte";
    import SelectItem from "$lib/components/ui/select/select-item.svelte";
    import SelectTrigger from "$lib/components/ui/select/select-trigger.svelte";
    
    let { options, value = $bindable() } = $props();
</script>

<div class="w-1/3 max-w-32">
    <Select type="single" bind:value>
        <SelectTrigger placeholder="Heloeawf">
            {value}
        </SelectTrigger>
        <SelectContent placeholder="Value">
            {#each options as option}
            <SelectItem value={option}></SelectItem>
            {/each}
        </SelectContent>
    </Select>
</div>
