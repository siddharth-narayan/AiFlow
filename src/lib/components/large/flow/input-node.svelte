<script lang="ts">
    import type { ModelType } from "$lib/api/triton/types";
    import { customHandlePosition } from "$lib/flow";
    import { Handle, Position, type NodeProps } from "@xyflow/svelte";

    let { data }: NodeProps = $props();

    let inputs = data.inputs as any[]
</script>

<div class="p-4 rounded bg-secondary">
  <p class="text-lg font-bold">Input(s)</p>

  {#each inputs as input, index}
    <Handle
      class="w-2"
      id={input.toString()}
      type="source"
      position={Position.Right}
      style={customHandlePosition(index, inputs.length)}
    />
    <div
      class="right-edge-label"
      style={customHandlePosition(index, inputs.length)}
    >
      <p class="font-bold">{input.toString()}</p>
      <!-- <p>{output.data_type} with dimension(s) [{output.dims.toString()}]</p> -->
    </div>
  {/each}
</div>

<style>
    .right-edge-label {
        position: absolute;
        right: 0;
        transform: translateX(110%) translateY(-50%);
    }
</style>
