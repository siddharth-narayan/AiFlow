<script lang="ts">
    import { customHandlePosition, inputs } from "$lib/flow";
    import { Handle, Position, useUpdateNodeInternals, type NodeProps } from "@xyflow/svelte";
    // import CustomHandle from "./custom-handle.svelte";
    import { v4 as uuid, v4} from "uuid"
    let _props: NodeProps = $props()

    const updateNodeInternals = useUpdateNodeInternals()
    inputs.subscribe(()=> {
      updateNodeInternals()
    })
</script>

<div class="p-4 rounded bg-secondary">
  <p class="text-lg font-bold">Input(s)</p>

  <!-- Ignore the type error for a bit, but eventually make $inputs from ModelType -->
  {#each $inputs as input, index}
    <Handle
        class="w-2"
        id={v4()}
        type="source"
        position={Position.Right}
        style={customHandlePosition(index, $inputs.length)}
    />
        <div
            class="left-edge-label"
            style={customHandlePosition(index, $inputs.length)}
        >
            <p class="font-bold">{input.name}</p>
            <p class="font-bold text-sm text-muted-foreground">
                {input.data_type}
            </p>  
          </div>
  {/each}
</div>