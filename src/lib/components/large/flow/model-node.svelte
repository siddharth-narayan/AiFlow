<script lang="ts">
  import type { ModelType } from "$lib/api/triton/types";
    import { customHandlePosition } from "$lib/flow";
  import { Handle, Position, type NodeProps } from "@xyflow/svelte";

  let { data }: NodeProps = $props();

  let model = data as ModelType;

</script>

<div class="p-4 rounded bg-secondary">
  <p>{model?.name}</p>
  {#each model.input as input, index}
    <Handle
      class="w-2"
      id={input.name}
      type="target"
      position={Position.Left}
      style={customHandlePosition(index, model.input.length)}
    />

    <div
      class="left-edge-label"
      style={customHandlePosition(index, model.input.length)}
    >
      <p class="font-bold">{input.name}</p>
      <!-- <p>{input.data_type} with dimension(s) [{input.dims.toString()}]</p> -->
    </div>
  {/each}

  {#each model.output as output, index}
    <Handle
      class="w-2"
      id={output.name}
      type="source"
      position={Position.Right}
      style={customHandlePosition(index, model.output.length)}
    />
    <div
      class="right-edge-label"
      style={customHandlePosition(index, model.output.length)}
    >
      <p class="font-bold">{output.name}</p>
      <!-- <p>{output.data_type} with dimension(s) [{output.dims.toString()}]</p> -->
    </div>
  {/each}
</div>

<style>
  .left-edge-label {
    position: absolute;
    left: 0;
    transform: translateX(-110%) translateY(-50%);
  }

  .right-edge-label {
    position: absolute;
    right: 0;
    transform: translateX(110%) translateY(-50%);
  }
</style>
