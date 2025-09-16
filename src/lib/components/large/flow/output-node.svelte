<script lang="ts">
    import { customHandlePosition, outputs } from "$lib/flow";
    import { Handle, Position, useUpdateNodeInternals, type NodeProps } from "@xyflow/svelte";
    import "./nodes.css"

    const updateNodeInternals = useUpdateNodeInternals()
    outputs.subscribe(()=> {
      updateNodeInternals()
    })
</script>

<div class="p-4 rounded bg-secondary">
  <p class="text-lg font-bold">Output</p>

  {#each $outputs as output, index}
    <Handle
      class="w-2"
      id={output.name}
      type="target"
      position={Position.Left}
      style={customHandlePosition(index, $outputs.length)}
    />
    <div
      class="left-edge-label"
      style={customHandlePosition(index, $outputs.length)}
    >
            <p class="font-bold">{output.name}</p>
      <p class="text-sm font-bold text-muted-foreground">{output.data_type}</p>
      <!-- <p>{output.data_type} with dimension(s) [{output.dims.toString()}]</p> -->
    </div>
  {/each}
</div>
