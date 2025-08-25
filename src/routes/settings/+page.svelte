<script lang="ts">
  import { z } from "zod";
  import ZxForm from "zxforms-svelte";

  let schema = z
    .object({
      tritonEndpoint: z
        .url({ message: "Please enter a valid url" })
        .meta({
          title: "Triton Endpoint",
          description: "Where is your triton server located?",
          placeholder: "https://api.example.com",
        }),
    })
    .meta({ title: "Settings" });

  schema.meta();
</script>

<div class="p-16">
  
<ZxForm {schema}></ZxForm>
</div>

