<script lang="ts">
  import { triton } from "$lib/api/triton/api";
  import Flow from "$lib/components/large/flow/flow.svelte";
    import { FlowElementType } from "$lib/flow";
    import { uuid } from "zod/mini";

  async function submit() {}

  // Svelte Flow stuff
  let nodes: {
    id: string;
    type: string;
    position: { x: number; y: number };
    data: any;
  }[] = $state([]);
  triton.ready.then(() => {
    triton.models;

    nodes = triton.models.map((model, index) => {
      return {
        id: model.name,
        type: "model",
        position: { x: 50, y: index * 50 + 50 },
        data: model,
      };
    });

    nodes.push({
      id: "input",
      type: "inputNode",
      position: { x: 0, y: 0 },
      data: {
        inputs: [],
      },
    });
  });

  let edges = $state([]);

  function addElementCallback(type: FlowElementType, data: string) {
    nodes.push({
      id: "aagagbs",
      type: type.toString(),
      position: { x: 0, y: 0},
      data: ""
    })
  }

</script>

<Flow bind:edges bind:nodes />
