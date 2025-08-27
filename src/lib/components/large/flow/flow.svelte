<script>
    import {
        Background,
        Controls,
        MiniMap,
        Panel,
        SvelteFlow,
    } from "@xyflow/svelte";
    import ModelNode from "./model-node.svelte";
    import { mode } from "mode-watcher";
    import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
    import { Plus } from "@lucide/svelte";
    import "@xyflow/svelte/dist/style.css";
    import { Button } from "$lib/components/ui/button";
    import { triton } from "$lib/api/triton/api";
    import InputNode from "./input-node.svelte";
    let { nodes = $bindable(), edges = $bindable() } = $props();
</script>

<SvelteFlow
    nodeTypes={{ model: ModelNode, inputNode: InputNode }}
    bind:nodes
    bind:edges
    colorMode={mode.current}
>
    <Background />
    <MiniMap />
    <Controls />
    <Panel>
        <DropdownMenu.Root>
            <DropdownMenu.Trigger>
                {#snippet child({ props })}
                    <Button {...props} variant="outline"
                        ><Plus />Add</Button
                    >
                {/snippet}
            </DropdownMenu.Trigger>
            <DropdownMenu.Content class="w-56" align="start">
                <!-- Add an input -->
                <DropdownMenu.Sub>
                    <DropdownMenu.SubTrigger
                        ><Plus />Add Input</DropdownMenu.SubTrigger
                    >
                    <DropdownMenu.SubContent>
                        {#await triton.ready then _}
                            {#each triton.models as model}
                                <DropdownMenu.Item
                                    >{model.name}</DropdownMenu.Item
                                >
                            {/each}
                        {/await}
                    </DropdownMenu.SubContent>
                </DropdownMenu.Sub>

                <!-- Add an output -->
                <DropdownMenu.Sub>
                    <DropdownMenu.SubTrigger
                        ><Plus />Add Output</DropdownMenu.SubTrigger
                    >
                    <DropdownMenu.SubContent>
                        {#await triton.ready then _}
                            {#each triton.models as model}
                                <DropdownMenu.Item
                                    >{model.name}</DropdownMenu.Item
                                >
                            {/each}
                        {/await}
                    </DropdownMenu.SubContent>
                </DropdownMenu.Sub>

                <!-- Add a model -->
                <DropdownMenu.Sub>
                    <DropdownMenu.SubTrigger
                        ><Plus />Add Model</DropdownMenu.SubTrigger
                    >
                    <DropdownMenu.SubContent>
                        {#await triton.ready then _}
                            {#each triton.models as model}
                                <DropdownMenu.Item
                                    >{model.name}</DropdownMenu.Item
                                >
                            {/each}
                        {/await}
                    </DropdownMenu.SubContent>
                </DropdownMenu.Sub>

                <!-- Add a tokenizer -->
                <DropdownMenu.Sub>
                    <DropdownMenu.SubTrigger
                        ><Plus />Add a Tokenizer</DropdownMenu.SubTrigger
                    >
                    <DropdownMenu.SubContent>
                        {#await triton.ready then _}
                            {#each triton.models as model}
                                <DropdownMenu.Item
                                    >{model.name}</DropdownMenu.Item
                                >
                            {/each}
                        {/await}
                    </DropdownMenu.SubContent>
                </DropdownMenu.Sub>
            </DropdownMenu.Content>
        </DropdownMenu.Root>
    </Panel>
</SvelteFlow>
