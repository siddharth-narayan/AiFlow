<script lang="ts">
    import {
        Background,
        Controls,
        MiniMap,
        Panel,
        SvelteFlow,
        type Connection,
    } from "@xyflow/svelte";
    import ModelNode from "./model-node.svelte";
    import { mode } from "mode-watcher";
    import "@xyflow/svelte/dist/style.css";
    import InputNode from "./input-node.svelte";
    import AddPanel from "./add-panel.svelte";
    import OutputNode from "./output-node.svelte";
    import { LoaderCircle } from "@lucide/svelte";
    import type { ModelType } from "$lib/api/triton/types";
    import { Play } from "lucide-svelte";
    import Button from "$lib/components/ui/button/button.svelte";
    import type { AnyNodeType} from "$lib/flow";
    import { inputs, outputs } from "$lib/flow"

    let {
        nodes = $bindable(),
        edges = $bindable(),
    }: { nodes: AnyNodeType[]; edges: any } = $props();

    function getFinalSourceType(node: AnyNodeType, connection: Connection) {
        let sourceType = undefined;

        if (node.type == "inputNode") {
            console.log("a")
            if (!connection.sourceHandle) {
                console.log("b")
                return;
            }

            $inputs.forEach((input) => {
                console.log(`${input.name} == ${connection.sourceHandle}`)
                if (input.name == connection.sourceHandle) {
                    sourceType = input.data_type;
                }
            });
            console.log("c")
            return sourceType;
        } else if (node.type == "modelNode"){
            let sourceInput = node.data.output.find((output) => {
                console.log(output)
                return output.name == connection.sourceHandle;
            });
            console.log("d")
            return sourceInput?.data_type
        }
    }

    function getFinalTargetType(node: AnyNodeType, connection: Connection) {
        let targetType = undefined;

        if (node.type == "outputNode") {
            if (!connection.targetHandle) {
                return;
            }

            $outputs.forEach((output) => {
                console.log(`${output.name} == ${connection.targetHandle}`)
                if (output.name == connection.targetHandle) {
                    targetType = output.data_type;
                }
            });

            return targetType;
        } else if (node.type == "modelNode"){
            console.log(node)
            let targetInput = node.data.input.find((input) => {
                return input.name == connection.targetHandle;
            });

            return targetInput?.data_type
        }
    }

    // This function really needs to be refactored
    function validateConnection(connection: Connection) {
        let source: AnyNodeType | undefined = nodes.find((node) => {
            return node.id == connection.source;
        });

        let target: AnyNodeType | undefined = nodes.find((node) => {
            return node.id == connection.target;
        });

        if (!source || !target) {
            return false;
        }

        let finalSourceType = getFinalSourceType(source, connection);
        let finalTargetType = getFinalTargetType(target, connection);

        console.log(finalSourceType)
        console.log(finalTargetType)
        return finalSourceType === finalTargetType ? connection : false;
    }

    let running = $state(false);

    function start() {
        running = true;
        setTimeout(() => {
            running = false;
        }, 10000);
        console.log("HAHE");
    }
</script>

<SvelteFlow
    nodeTypes={{
        modelNode: ModelNode,
        inputNode: InputNode,
        outputNode: OutputNode,
    }}
    bind:nodes
    bind:edges
    onbeforeconnect={validateConnection}
    colorMode={mode.current}
>
    <!--  onbeforeconnect={validateConnection} -->
    <Background />
    <!-- <MiniMap /> -->
    <Controls />
    <AddPanel />
    <Panel position="bottom-right">
        {#if !running}
            <Button onclick={start} variant="constructive"
                >Start <Play /></Button
            >
        {:else}
            <Button variant="secondary" disabled
                >Running <LoaderCircle class="animate-spin" /></Button
            >
        {/if}
    </Panel>
</SvelteFlow>
