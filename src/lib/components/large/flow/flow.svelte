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
    import { Play } from "lucide-svelte";
    let { nodes = $bindable(), edges = $bindable(), callback } = $props();

    function start() {
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
        <Button onclick={start} variant="constructive">Start <Play /></Button>
    </Panel>
</SvelteFlow>