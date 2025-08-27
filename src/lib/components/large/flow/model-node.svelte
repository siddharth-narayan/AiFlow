<script lang="ts">
  import type { ModelType } from "$lib/api/triton/types";
  import { Handle, Position, type NodeProps } from "@xyflow/svelte";

  let { data }: NodeProps = $props();


  let model = data as ModelType;

  console.log(model);

  // Returns a string percentage to style the correct position on a handle 
  function customHandlePosition(index: number, count: number){
    let even = count % 2 == 0
    let globalPosition = 50; // The placement of the center of all the handles
    let handleHeight = 70; // Total height (percentage) of all the handles
    
    let distance = handleHeight / count

    // Minimum 10% distance
    distance = distance < 10 ? 10 : distance 
    
    let firstHandlePosition = globalPosition - ((count - 1) * distance / 2)
    // Position of the specific handle
    let position = firstHandlePosition + index * distance

    return `top:${position}%;`
  }

  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < i; j++) {
      console.log(`index: ${j} count: ${i} position: ${customHandlePosition(j, i)}`)

    }
    
  }
</script>

<div class="p-4 rounded bg-secondary">
  <p>{model?.name}</p>
  {#each model.input as input, index}
  <Handle class="w-2" id={input.name} type="target" position={Position.Left} style={customHandlePosition(index, model.input.length)}/>
  <p class="left-edge-label" style={customHandlePosition(index, model.input.length)}>{input.name}</p>
  {/each}

  {#each model.output as output, index}
  <Handle class="w-2" id={output.name} type="source" position={Position.Right} style={customHandlePosition(index, model.output.length)}/>
  <p class="right-edge-label" style={customHandlePosition(index, model.output.length)}>{output.name}</p>
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