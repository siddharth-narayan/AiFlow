<script lang="ts">
  import type { ModelType } from "$lib/api/triton/types";
  import { Handle, Position, type NodeProps } from "@xyflow/svelte";

  let { data }: NodeProps = $props();


  let model = data as ModelType;

  console.log(model);
</script>

<div class="p-4 border-border border-2 text-accent">
  <p>{model?.name}</p>
  <p>ahao</p>
  <Handle type="target" position={Position.Left} />
  <Handle type="source" position={Position.Right} />
</div>
