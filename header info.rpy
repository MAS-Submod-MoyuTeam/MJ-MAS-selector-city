#credit to my-otter-self / your-otter-friend for help with the repo, creds to raVen and (sigh) ATOM_real for original selector code to base all these on

init -990 python in mas_submod_utils:
    Submod(
        author="MayJay",
        name="Selector City",
        description="由 u/mayday-mayjay 维护的一组精灵包选择器. Discord: https://discord.gg/Tx23rczN8N ",
        version="1.0.2",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MayJay's Selector City",
            user_name="mayday-mayjay",
            repository_name="MJ-MAS-selector-city",
            submod_dir="/Submods/Selector City",
            extraction_depth=3,
            redirected_files=(
                "README.md"
            )
        )
