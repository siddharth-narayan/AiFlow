<script lang="ts">
  import "../app.css";
  import SettingsIcon from "@lucide/svelte/icons/settings";
  import { ModeWatcher } from "mode-watcher";
  import ThemeSwitcher from "$lib/components/large/theme-switcher.svelte";
  import * as Sidebar from "$lib/components/ui/sidebar/index.js";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import ChevronDown from "@lucide/svelte/icons/chevron-down";
  import SearchIcon from "@lucide/svelte/icons/search";
  import { Collapsible } from "bits-ui";
  
  let { children } = $props();
  
  let groups = [
    {
      title: "Settings",
      icon: SettingsIcon,
      collapsible: true,
      items: [
        { title: "piece", link: "#", icon: SearchIcon }
      ]
    }
  ];
</script>

<ModeWatcher />

<div class="flex gap-4">
  <Sidebar.Provider style="--sidebar-width: 20rem;">
    <Sidebar.Root>
      <Sidebar.Header></Sidebar.Header>
      <Sidebar.Content>
        {#each groups as group}
          {#if group.collapsible}
            <Collapsible.Root class="group/collapsible">
              <Sidebar.Group>
                <Sidebar.GroupLabel
                  class="hover:bg-sidebar-accent hover:text-sidebar-accent-foreground text-sm"
                >
                  {#snippet child({ props })}
                    <Collapsible.Trigger {...props}>
                      <group.icon class="mr-2"/>
                        
                      {group.title}
                      <ChevronDown
                        class="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-180"
                      />
                    </Collapsible.Trigger>
                  {/snippet}
                </Sidebar.GroupLabel>
                <Collapsible.Content>
                  <Sidebar.GroupContent>
                    <Sidebar.Menu>
                      {#each group.items as item}
                        <Sidebar.MenuItem>
                          <Sidebar.MenuButton>
                            {#snippet child({ props })}
                              <a href={item.link} {...props}>
                                <item.icon />
                                <span>{item.title}</span>
                              </a>
                            {/snippet}
                          </Sidebar.MenuButton>
                        </Sidebar.MenuItem>
                      {/each}
                    </Sidebar.Menu>
                  </Sidebar.GroupContent>
                </Collapsible.Content>
              </Sidebar.Group>
            </Collapsible.Root>
          {:else}
            <Sidebar.Group>
              <Sidebar.GroupLabel>{group.title}</Sidebar.GroupLabel>
            </Sidebar.Group>
          {/if}
        {/each}
      </Sidebar.Content>
      <Sidebar.Footer>
        <ThemeSwitcher />
        <p class="text-gray-500">Version 1.0</p>
      </Sidebar.Footer>
    </Sidebar.Root>
    <Sidebar.Trigger />
  </Sidebar.Provider>

  <div class="w-full">
    {@render children()}
  </div>
</div>
