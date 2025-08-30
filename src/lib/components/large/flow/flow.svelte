<script lang="ts">
    import {
        Background,
        Controls,
        MiniMap,
        SvelteFlow,
    } from "@xyflow/svelte";
    import ModelNode from "./model-node.svelte";
    import { mode } from "mode-watcher";
    import "@xyflow/svelte/dist/style.css";
    import InputNode from "./input-node.svelte";
    import AddPanel from "./add-panel.svelte";
    import OutputNode from "./output-node.svelte";
    let { nodes = $bindable(), edges = $bindable() } = $props();
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
</SvelteFlow>