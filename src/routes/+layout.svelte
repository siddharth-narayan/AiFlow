<script lang="ts">
  import "../app.css";

  import {
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarHeader,
    SidebarMenu,
    SidebarProvider,
    SidebarTrigger,
  } from "$lib/components/ui/sidebar";
  import SettingsIcon from "@lucide/svelte/icons/settings";
  import { ModeWatcher } from "mode-watcher";
  import ThemeSwitcher from "$lib/components/large/theme-switcher.svelte";
  import SidebarMenuItem from "$lib/components/ui/sidebar/sidebar-menu-item.svelte";
  import SidebarGroupLabel from "$lib/components/ui/sidebar/sidebar-group-label.svelte";
  import SidebarGroupContent from "$lib/components/ui/sidebar/sidebar-group-content.svelte";
  import SidebarMenuButton from "$lib/components/ui/sidebar/sidebar-menu-button.svelte";

  let { children } = $props();

  let items = {
	
  }
</script>

<ModeWatcher />

<div class="flex gap-4">
  <SidebarProvider style="--sidebar-width: 20rem;">
    <Sidebar>
      <SidebarHeader></SidebarHeader>
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Application</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              <SidebarMenuItem>
                <SidebarMenuButton
                  ><SettingsIcon>

				  </SettingsIcon>
				  <a href="/settings">Settings</a></SidebarMenuButton
                >
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
      <SidebarFooter>
        <ThemeSwitcher />
      </SidebarFooter>
    </Sidebar>
    <SidebarTrigger />
  </SidebarProvider>

  <div class="w-full">
    {@render children()}
  </div>
</div>
