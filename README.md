# Relaxed Theme for Zed

> A relaxed Zed theme to take a more relaxed view of things.

A port of the [Relaxed theme for Visual Studio Code](https://github.com/Relaxed-Theme/vscode-theme-relaxed) to [Zed](https://zed.dev).

<img width="2688" height="1554" alt="Screenshot: Relaxed theme in Zed" src="https://github.com/user-attachments/assets/86256822-e557-4c72-9c1f-d7424f2abee1" />

## Installation

1. Open **Extensions** in Zed (`cmd-shift-x` on macOS)
2. Search for `Relaxed`
3. Click **Install**
4. Open the theme picker (`cmd-k cmd-t`) and select **Relaxed**

## I don't like something

If something looks funky, please [open an issue](https://github.com/Relaxed-Theme/zed-theme-relaxed/issues).

If you would like to change something, you can either open a PR and see if we'd like it added, or override the colors in your own `settings.json`:

```json
"theme_overrides": {
  "Relaxed": {
    "search.match_background": "#ebc17a40"
  }
}
```

<https://zed.dev/docs/themes>

### Contributing

#### Get up and running straight away

* Fork and clone this repository
* In Zed, open the **Extensions** page (`cmd-shift-x`), click **Install Dev Extension** and select the cloned directory
* Open the theme picker (`cmd-k cmd-t`) and pick the »Relaxed« color theme

#### Make changes

* All colors live in [`themes/relaxed.json`](themes/relaxed.json)
* After editing, click **Rebuild** next to the dev extension on the **Extensions** page to load your changes
* Available keys are listed in the [theme schema](https://zed.dev/schema/themes/v0.2.0.json). To learn more, check out the [theme extension](https://zed.dev/docs/extensions/themes) documentation.

#### Remove the dev extension

* Click **Uninstall** next to the dev extension on the **Extensions** page
* Reinstall the published **Relaxed** extension if you had it installed before

## Color Palette

| Role | Color |
|---|---|
| Background | `#2e333b` |
| Editor foreground | `#d9d9d9` |
| Keywords | `#b06698` |
| Control keywords (`if`, `return`, `import`) | `#6a8799` |
| Functions | `#7eaac7` |
| Strings | `#909d63` |
| Types / Classes | `#ebc17a` |
| Built-in constants (`None`, `null`, `true`) | `#b06698` |
| Tags | `#bc5653` |
| Comments | `#727272` |
| Variables, properties, `ALL_CAPS` constants | `#d9d9d9` |
| Parameters | `#b06698` |
| Operators | `#6a8799` |
| Regex / Escape, SCSS variables | `#acbbd0` |
| Markdown headings | `#ebc17a` |
| Markdown links / URLs | `#6894c1` / `#f78c6c` |

## Related

* [Relaxed theme for Visual Studio Code](https://github.com/Relaxed-Theme/vscode-theme-relaxed) - The original.
* [Relaxed theme for Terminal](https://github.com/Relaxed-Theme/relaxed-terminal-themes) - For iTerm, Hyper, the macOS Terminal and a bunch of others.

## License

Zed port by Stefan Cosma, original theme by Michael Kühnel.

[MIT License](LICENSE)
