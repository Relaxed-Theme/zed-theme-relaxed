# Hammock List

A calm little document to showcase the **Relaxed** theme in *Markdown*, with ~~stress~~ nested formatting everywhere.

## Getting started

Install the package with `npm install hammock-list` and import the **`HammockList`** component. See the [API reference](https://example.com/docs "Hammock docs") or the [**`fetchHammocks()`** helper](#api) for details.

- **`backticked` in bold.**
- *`backticked` in italics*, and ***`backticked` in bold italics***
- **Bold with *nested italics* and a [link](https://example.com)**
- ~~**Bold and struck through** with `code`~~
  - Nested item with _underscore emphasis_ and __underscore bold__
  - [**Bold link with `code`**](https://example.com/hammocks)
    1. Ordered item with a footnote[^swing]
    2. Ordered item with an inline image ![hammock icon](./hammock.svg)

### Checklist

- [x] Hang up the **hammock**
- [ ] Brew some *tea* using `brew --gently`
- [ ] Take a nap, ~~check emails~~

> **Note:** A hammock is only relaxing if it is `swinging` *gently*.
>
> > Nested quote with a [link to calm](https://example.com/calm) and **bold `code`**.

## API

| Prop      | Type      | Default | Description                         |
| --------- | --------- | :-----: | ----------------------------------- |
| `title`   | `string`  |   n/a   | **Required.** Heading of the list   |
| `limit`   | `number`  |  `10`   | Maximum number of *hammocks* shown  |
| `swinging`| `boolean` | `false` | Only show hammocks that are moving  |

```tsx
import { HammockList } from "hammock-list";

export const App = () => <HammockList title="Relax" limit={5} />;
```

```bash
# Run the Python version
python hammock_list.py --limit 5
```

---

Made with ☕ and <kbd>Ctrl</kbd> + <kbd>Z</kbd>. Visit <https://example.com> for more.

[^swing]: Swinging is optional, but **highly** recommended.
