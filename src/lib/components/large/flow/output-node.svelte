<script lang="ts">
    import { customHandlePosition, outputs } from "$lib/flow";
    import {
    Handle,
        Position,
        useUpdateNodeInternals,
        type NodeProps,
    } from "@xyflow/svelte";
    import "./nodes.css";
    import { v4 } from "uuid";

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
<Handle
    class="w-2"
    id={v4()}
    type="target"
    position={Position.Left}
    style={customHandlePosition(index, $outputs.length)}
/>
    <div
        class="left-edge-label"
        style={customHandlePosition(index, $outputs.length)}
    >
        <p class="font-bold">{output.name}</p>
        <p class="font-bold text-sm text-muted-foreground">
            {output.data_type}
        </p>
    </div>
    {/each}
</div>
