<script lang="ts">
    import {
        Background,
        Controls,
        MiniMap,
        Panel,
        SvelteFlow,
    } from "@xyflow/svelte";
    import ModelNode from "./model-node.svelte";
    import { mode } from "mode-watcher";
    import "@xyflow/svelte/dist/style.css";
    import InputNode from "./input-node.svelte";
    import AddPanel from "./add-panel.svelte";
    import OutputNode from "./output-node.svelte";
    import Button from "$lib/components/ui/button/button.svelte";
    import { Loader2Icon, Play } from "lucide-svelte";
    import { LoaderCircle } from "@lucide/svelte";
    let { nodes = $bindable(), edges = $bindable(), callback } = $props();


    let running = $state(false);

    function start() {
        running = true
        setTimeout(()=>{running = false}, 1000)
        console.log("HAHE")
    }
</script>

<SvelteFlow
    nodeTypes={{
        model: ModelNode,
        inputNode: InputNode,
        outputNode: OutputNode,
    }}
    bind:nodes
    bind:edges
    colorMode={mode.current}
>
    <Background />
    <!-- <MiniMap /> -->
    <Controls />
    <AddPanel />
    <Panel position="bottom-right">
        {#if !running}
            <Button onclick={start} variant="constructive">Start <Play /></Button>
        {:else}
            
            <Button variant="secondary" disabled>Running <LoaderCircle class="animate-spin" /></Button>
        {/if}
    </Panel>
</SvelteFlow>