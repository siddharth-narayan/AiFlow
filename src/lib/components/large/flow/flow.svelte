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
    import type { ModelType } from "$lib/api/triton/types";
    import { Play } from "lucide-svelte";
    import Button from "$lib/components/ui/button/button.svelte";
    type NodesType = {
        id: string;
        type: string;
        position: {
            x: number;
            y: number;
        };
        data: any;
    }[];

    let { nodes = $bindable(), edges = $bindable() }: {nodes: NodesType, edges: any}= $props();

    function validateConnection(connection: Connection) {
        let finalSourceType = ""
        let finalTargetType = ""
        
        console.log("Validating connection")
        let source = nodes.find((node) => {
            return node.id == connection.source
        })

        let target = nodes.find((node) => {
            return node.id == connection.target
        })
        
        if (!source || !target) {
            return false;
        }

        if (source.type == "inputNode") {
            if (!connection.sourceHandle) {
                return
            }

            finalSourceType = "";
        }

        console.log(source)
        console.log(source.data)
        let sourceInput = (source.data as ModelType).input.find((input)=>{
            input.name == connection.sourceHandle
        })

        console.log(target.data)
        let targetInput = (target.data as ModelType).input.find((input)=>{
            input.name == connection.sourceHandle
        })

        console.log(sourceInput)

        connection
    
    }

    function start() {
        console.log("HAHE")
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
    <Background />
    <!-- <MiniMap /> -->
    <Controls />
    <AddPanel />
    <Panel position="bottom-right">
        <Button onclick={start} variant="constructive">Start <Play /></Button>
    </Panel>
</SvelteFlow>
