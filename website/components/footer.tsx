import Link from 'next/link';
import { Github, FileText, ExternalLink } from 'lucide-react';

export function Footer() {
  return (
    <footer className="border-t mt-20 py-16 bg-muted/50">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
          <div className="md:col-span-2">
            <h3 className="font-bold text-2xl mb-4">typesim</h3>
            <p className="text-muted-foreground leading-relaxed mb-4">
              AI-powered Python tool for simulating authentic human typing patterns. 
              Bypass typing analysis systems with realistic typos, corrections, and natural pauses.
            </p>
            <p className="text-sm text-muted-foreground">
              Use responsibly and comply with platform rules.
            </p>
          </div>
          <div>
            <h3 className="font-bold text-lg mb-4">Resources</h3>
            <ul className="space-y-3">
              <li>
                <Link href="/docs" className="text-foreground hover:text-primary transition-colors flex items-center gap-2">
                  <FileText className="w-4 h-4" />
                  Documentation
                </Link>
              </li>
              <li>
                <a
                  href="https://github.com/pc-style/typesim"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-foreground hover:text-primary transition-colors flex items-center gap-2"
                >
                  <Github className="w-4 h-4" />
                  GitHub
                </a>
              </li>
              <li>
                <a
                  href="https://pcstyle.dev"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-foreground hover:text-primary transition-colors flex items-center gap-2"
                >
                  <ExternalLink className="w-4 h-4" />
                  pcstyle.dev
                </a>
              </li>
            </ul>
          </div>
          <div>
            <h3 className="font-bold text-lg mb-4">Legal</h3>
            <ul className="space-y-3">
              <li className="text-muted-foreground">MIT License</li>
              <li className="text-muted-foreground">Open Source</li>
            </ul>
          </div>
        </div>
        <div className="border-t pt-8 text-center">
          <p className="text-muted-foreground font-medium">
            © {new Date().getFullYear()} typesim by <a href="https://pcstyle.dev" target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">pcstyle.dev</a>
          </p>
        </div>
      </div>
    </footer>
  );
}

