	
<script lang="ts">
	import "../app.css";

    import { Button } from "$lib/components/ui/button";
	import Sun from "@lucide/svelte/icons/sun";
	import Moon from "@lucide/svelte/icons/moon";

	import { ModeWatcher } from "mode-watcher";
	let { children } = $props();
  </script>
   
  <ModeWatcher />
  {@render children()}
  
