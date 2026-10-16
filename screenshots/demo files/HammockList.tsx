import { useEffect, useState, type ReactNode } from "react";

// A calm little component to showcase the Relaxed theme
enum Mood {
  Chill = "chill",
  Sleepy = "sleepy",
}

const foo = null;

interface Hammock<T = string> {
  id: number;
  label: T;
  mood: Mood;
  swinging?: boolean;
}

type Props = { title: string; limit?: number; children?: ReactNode };

const API_URL = "https://api.example.com/hammocks";
const SLUG_PATTERN = /^[a-z0-9-]+$/i;

async function fetchHammocks(limit: number): Promise<Hammock[]> {
  const res = await fetch(`${API_URL}?limit=${limit}`);
  if (!res.ok) throw new Error(`Request failed: ${res.status}`);
  return res.json();
}

export function HammockList({ title, limit = 10, children }: Props) {
  const [items, setItems] = useState<Hammock[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetchHammocks(limit)
      .then(setItems)
      .finally(() => setIsLoading(false));
  }, [limit]);

  const swinging = items.filter((item) => item.swinging);

  return (
    <section className="hammock-list" aria-busy={isLoading}>
      <h1>{title}</h1>
      {isLoading ? (
        <p className="hint">Brewing some tea…</p>
      ) : (
        <ul>
          {items.map(({ id, label, mood }) => (
            <li key={id} hidden={!SLUG_PATTERN.test(label)}>
              {label} <small>({mood})</small>
            </li>
          ))}
        </ul>
      )}
      <footer>{swinging.length} of {items.length} swinging</footer>
      {children}
    </section>
  );
}
