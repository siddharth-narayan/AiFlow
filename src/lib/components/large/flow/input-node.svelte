<script lang="ts">
    import { customHandlePosition, inputs } from "$lib/flow";
    import "./nodes.css"
    import { Handle, Position, useUpdateNodeInternals, type NodeProps } from "@xyflow/svelte";

    const updateNodeInternals = useUpdateNodeInternals()
    inputs.subscribe(()=> {
      updateNodeInternals()
    })
</script>

<div class="p-4 rounded bg-secondary">
  <p class="text-lg font-bold">Input(s)</p>

  {#each $inputs as input, index}
    <Handle
      class="w-2"
      id={input.name} 
      type="source"
      position={Position.Right}
      style={customHandlePosition(index, $inputs.length)}
    />
    <div
      class="right-edge-label"
      style={customHandlePosition(index, $inputs.length)}
    >
      <p class="font-bold">{input.name}</p>
      <p class="text-sm font-bold text-muted-foreground">{input.data_type}</p>
    </div>
  {/each}
</div>