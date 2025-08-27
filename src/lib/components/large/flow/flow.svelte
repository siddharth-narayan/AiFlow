<script>
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
    let { nodes = $bindable(), edges = $bindable() } = $props();
</script>

<SvelteFlow
    nodeTypes={{ model: ModelNode, inputNode: InputNode }}
    bind:nodes
    bind:edges
    colorMode={mode.current}
>
    <Background />
    <MiniMap />
    <Controls />
    <AddPanel/>
</SvelteFlow>
