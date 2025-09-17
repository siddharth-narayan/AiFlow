<script lang="ts">
    import { outputs } from "$lib/flow";
    import {
        Position,
        useUpdateNodeInternals,
        type NodeProps,
    } from "@xyflow/svelte";
    import "./nodes.css";
    import CustomHandle from "./custom-handle.svelte";

    let _props: NodeProps = $props();

    const updateNodeInternals = useUpdateNodeInternals();
    outputs.subscribe(() => {
        updateNodeInternals();
    });
</script>

<div class="p-4 rounded bg-secondary">
    <p class="text-lg font-bold">Output</p>

    <!-- Ignore the type error for a bit, but eventually make $inputs from ModelType -->
    {#each $outputs as output, index}
        <CustomHandle
            handleIO={output}
            type={"target"}
            handleIndex={index}
            handleTotal={$outputs.length}
            position={Position.Left}
        />
    {/each}
</div>
