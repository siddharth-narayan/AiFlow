<script lang="ts">
  import { triton } from "$lib/api/triton/api";
  import Flow from "$lib/components/large/flow/flow.svelte";

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
      position: { x: 200, y: 200 },
      data: {
        inputs: [],
      },
    }, {
      id: "output",
      type: "outputNode",
      position: { x: 500, y: 200 },
      data: {
        inputs: [],
      },
    });
  });

  let edges = $state([]);

</script>

<Flow bind:edges bind:nodes />
