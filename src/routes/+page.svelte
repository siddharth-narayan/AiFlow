<script lang="ts">
  import { schemaFetch } from "$lib/api/fetcher";
  import {
    modelIndexResponse,
    modelInfoResponse,
  } from "$lib/api/triton-inference-schema";
  import AiMediaInput from "$lib/components/large/ai-media-input.svelte";
  import AiMediaOutput from "$lib/components/large/ai-media-output.svelte";
  import SingleSelect from "$lib/components/large/single-select.svelte";

  import { Separator } from "$lib/components/ui/separator/index.js";
  import { json } from "@sveltejs/kit";
  import { onMount } from "svelte";
  import { z } from "zod";

  let media_type_1 = $state("text");
  let media_type_2 = $state("text");
  let selectedModel = $state("");
  let availableModels: z.infer<typeof modelInfoResponse>[];

  let mediaTypes = new Map();
  mediaTypes.set("audio", "BYTES");
  mediaTypes.set("video", "BYTES");
  mediaTypes.set("text", "TYPE_STRING");
  mediaTypes.set("3D", "BYTES");

  onMount(() => {
    availableModels = $derived(getAvailableModels(mediaTypes.get("text"), mediaTypes.get("text")))
        //.then((models)=> {selectedModel = models[0].name})
  });

  let tritonEndpoint = "test.novaphaze.com";
  async function getAvailableModels(
    inputTypeRequired: string,
    outputTypeRequired: string
  ) {
    let models = modelIndexResponse.parse(
      await (
        await fetch(`https://${tritonEndpoint}/v2/repository/index`, {
          method: "POST",
        })
      ).json()
    );

    let availableModels = models.filter(async (model) => {
      let info = await schemaFetch(
        `https://${tritonEndpoint}/v2/models/${model.name}/config`,
        modelInfoResponse
      );

      let containsCorrectInput =
        info.input.filter((input) => {
          input.data_type == inputTypeRequired;
        }).length > 0;
      let containsCorrectOutput =
        info.output.filter((output) => {
          output.data_type == outputTypeRequired;
        }).length > 0;

      return (
        containsCorrectInput && containsCorrectOutput && model.state == "READY"
      );
    });

    return availableModels;
  }
</script>

<div class="flex justify-center items-center gap-4 p-4">
  <!-- svelte-ignore block_empty -->
  {#await getAvailableModels(mediaTypes.get(media_type_1), mediaTypes.get(media_type_2)) then models}
    {#if models.length > 0}
      <label>Model: </label>
      <SingleSelect
        value={selectedModel}
        options={models.map((model) => model.name)}
      />
    {/if}
  {/await}
</div>

<div class="flex gap-4 p-4 h-full">
  <div class="w-1/2 flex flex-col gap-4 items-center">
    <SingleSelect bind:value={media_type_1} options={mediaTypes.keys()}
    ></SingleSelect>
    <AiMediaInput type={media_type_1} />
  </div>
  <Separator orientation="vertical" />
  <div class="w-1/2 flex flex-col gap-4 items-center">
    <SingleSelect bind:value={media_type_2} options={mediaTypes.keys()}
    ></SingleSelect>
    <AiMediaOutput type={media_type_1} interactive={false} />
  </div>
</div>
