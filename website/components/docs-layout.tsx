'use client';

import { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Button } from '@/components/ui/button';
import { Menu, X, Github } from 'lucide-react';
import { useTheme } from 'next-themes';

const docsNav = [
  { title: 'Getting Started', href: '/docs/getting-started' },
  { title: 'Installation', href: '/docs/installation' },
  { title: 'Configuration', href: '/docs/configuration' },
  { title: 'Usage', href: '/docs/usage' },
  { title: 'API', href: '/docs/api' },
  { title: 'Examples', href: '/docs/examples' },
];

interface DocsLayoutProps {
  children: React.ReactNode;
}

export function DocsLayout({ children }: DocsLayoutProps) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const pathname = usePathname();
  const { theme, setTheme } = useTheme();

  return (
    <div className="min-h-screen flex flex-col">
      {/* Topbar */}
      <header className="border-b-4 border-foreground bg-background sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4 flex items-center justify-between">
          <Link href="/" className="font-bold text-xl">
            typesim
          </Link>
          <div className="flex items-center gap-4">
            <a
              href="https://github.com/pc-style/typesim"
              target="_blank"
              rel="noopener noreferrer"
              className="p-2 hover:bg-muted rounded"
            >
              <Github className="w-5 h-5" />
            </a>
            <Button
              variant="outline"
              size="sm"
              onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            >
              {theme === 'dark' ? '☀️' : '🌙'}
            </Button>
            <Button
              variant="ghost"
              size="sm"
              className="md:hidden"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            >
              {mobileMenuOpen ? <X /> : <Menu />}
            </Button>
          </div>
        </div>
      </header>

      <div className="flex flex-1">
        {/* Sidebar */}
        <aside
          className={`
            w-64 border-r-4 border-foreground bg-muted/50 p-6
            fixed md:sticky top-[73px] h-[calc(100vh-73px)] overflow-y-auto
            ${mobileMenuOpen ? 'block' : 'hidden md:block'}
            z-40
          `}
        >
          <nav className="space-y-2">
            {docsNav.map((item) => {
              const isActive = pathname === item.href;
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  className={`
                    block px-4 py-2 rounded font-medium transition-colors
                    ${
                      isActive
                        ? 'bg-primary text-primary-foreground'
                        : 'hover:bg-muted'
                    }
                  `}
                  onClick={() => setMobileMenuOpen(false)}
                >
                  {item.title}
                </Link>
              );
            })}
          </nav>
        </aside>

        {/* Main content */}
        <main className="flex-1 p-8 md:p-12 max-w-4xl mx-auto w-full">
          {children}
        </main>
      </div>
    </div>
  );
}

