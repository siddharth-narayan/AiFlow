<script lang="ts">
    import { inputs } from "$lib/flow";
    import { Handle, Position, useUpdateNodeInternals, type NodeProps } from "@xyflow/svelte";
    import CustomHandle from "./custom-handle.svelte";

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
    <CustomHandle handleIO={input} type={"source"} handleIndex={index} handleTotal={$inputs.length} position={Position.Right}/>
  {/each}
</div>