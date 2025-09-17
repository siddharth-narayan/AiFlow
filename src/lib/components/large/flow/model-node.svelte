<script lang="ts">
  import type { ModelType } from "$lib/api/triton/types";
  import { Position, type NodeProps } from "@xyflow/svelte";
    import CustomHandle from "./custom-handle.svelte";
  
  let { data }: NodeProps = $props();

  let model = data as ModelType;

</script>

<div class="p-4 rounded bg-secondary">
  <p>{model?.name}</p>
  {#each model.input as input, index}
    <CustomHandle type={"target"} handleIO={input} handleIndex={index} handleTotal={model.input.length} position={Position.Left}/>
  {/each}

  {#each model.output as output, index}
    <CustomHandle type={"source"} handleIO={output} handleIndex={index} handleTotal={model.input.length} position={Position.Right}/>
  {/each}
</div>