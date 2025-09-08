<script lang="ts">
    import { Panel } from "@xyflow/svelte";
    import { Button } from "$lib/components/ui/button";
    import { triton } from "$lib/api/triton/api";

    import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
    import { Plus } from "@lucide/svelte";
    import type { DataType } from "$lib/api/triton/types";
    import { inputs, outputs } from "$lib/flow";

    function addInput(type: DataType) {
        let temp = $inputs
        temp.push({
            name: `flow-input-${$inputs.length.toString()}`,
            data_type: type
        })

        $inputs = temp
    }

        function addOutput(type: DataType) {
        let temp = $outputs
        temp.push({
            name: `flow-output-${$inputs.length.toString()}`,
            data_type: type
        })

        $outputs = temp
    }
</script>

<Panel>
    <DropdownMenu.Root>
        <DropdownMenu.Trigger>
            {#snippet child({ props })}
                <Button {...props} variant="outline"><Plus />Add</Button>
            {/snippet}
        </DropdownMenu.Trigger>
        <DropdownMenu.Content class="w-56" align="start">
            <!-- Add an input -->
            <DropdownMenu.Sub>
                <DropdownMenu.SubTrigger><Plus />Input</DropdownMenu.SubTrigger>
                <DropdownMenu.SubContent>
                    <DropdownMenu.Item onclick={()=>addInput("TYPE_BYTES")}>File</DropdownMenu.Item>
                    <DropdownMenu.Item onclick={()=>addInput("TYPE_STRING")}>Text</DropdownMenu.Item>
                    <DropdownMenu.Item onclick={()=>addInput("TYPE_BYTES")}>Video</DropdownMenu.Item>
                    <DropdownMenu.Item onclick={()=>addInput("TYPE_BYTES")}>Audio</DropdownMenu.Item>
                </DropdownMenu.SubContent>
            </DropdownMenu.Sub>

            <!-- Add an output -->
            <DropdownMenu.Sub>
                <DropdownMenu.SubTrigger><Plus />Output</DropdownMenu.SubTrigger
                >
                <DropdownMenu.SubContent>
                    <DropdownMenu.Item onclick={()=>addOutput("TYPE_BYTES")}>File</DropdownMenu.Item>
                    <DropdownMenu.Item onclick={()=>addOutput("TYPE_STRING")}>Text</DropdownMenu.Item>
                    <DropdownMenu.Item onclick={()=>addOutput("TYPE_BYTES")}>Video</DropdownMenu.Item>
                    <DropdownMenu.Item onclick={()=>addOutput("TYPE_BYTES")}>Audio</DropdownMenu.Item>
                </DropdownMenu.SubContent>
            </DropdownMenu.Sub>

            <!-- Add a model -->
            <DropdownMenu.Sub>
                <DropdownMenu.SubTrigger><Plus />Model</DropdownMenu.SubTrigger>
                <DropdownMenu.SubContent>
                    {#await triton.ready then _}
                        {#each triton.models as model}
                            <DropdownMenu.Item>{model.name}</DropdownMenu.Item>
                        {/each}
                    {/await}
                </DropdownMenu.SubContent>
            </DropdownMenu.Sub>

            <!-- Add a tokenizer -->
            <DropdownMenu.Sub>
                <DropdownMenu.SubTrigger
                    ><Plus />Tokenizer</DropdownMenu.SubTrigger
                >
                <DropdownMenu.SubContent>
                    {#await triton.ready then _}
                        {#each triton.models as model}
                            <DropdownMenu.Item>{model.name}</DropdownMenu.Item>
                        {/each}
                    {/await}
                </DropdownMenu.SubContent>
            </DropdownMenu.Sub>
        </DropdownMenu.Content>
    </DropdownMenu.Root>
</Panel>
