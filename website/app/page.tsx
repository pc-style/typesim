import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { FeatureCard } from '@/components/feature-card';
import { TypingDemo } from '@/components/typing-demo';
import { CodeBlock } from '@/components/code-block';
import { Terminal } from '@/components/terminal';
import { Footer } from '@/components/footer';
import { Github, Zap, Brain, Keyboard, FileText, Settings } from 'lucide-react';

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      {/* Navigation */}
      <nav className="border-b-4 border-foreground bg-background sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4 flex items-center justify-between">
          <Link href="/" className="font-bold text-2xl">
            typesim
          </Link>
          <div className="flex items-center gap-4">
            <Link href="/docs">
              <Button variant="ghost">Docs</Button>
            </Link>
            <a
              href="https://github.com/pc-style/typesim"
              target="_blank"
              rel="noopener noreferrer"
            >
              <Button variant="outline">
                <Github className="w-4 h-4 mr-2" />
                GitHub
              </Button>
            </a>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="container mx-auto px-4 py-20 md:py-32">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-5xl md:text-7xl font-bold mb-6">
            Realistic Typing
            <br />
            <span className="text-primary">Simulator</span>
          </h1>
          <p className="text-xl md:text-2xl text-muted-foreground mb-8">
            AI-driven typing behavior for Python. Make your typing look natural
            with typos, corrections, and thinking pauses.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/docs">
              <Button size="lg" className="neo-border-thick text-lg px-8 py-6">
                Get Started
              </Button>
            </Link>
            <a
              href="https://github.com/pc-style/typesim"
              target="_blank"
              rel="noopener noreferrer"
            >
              <Button
                size="lg"
                variant="outline"
                className="neo-border text-lg px-8 py-6"
              >
                View on GitHub
              </Button>
            </a>
          </div>
        </div>
      </section>

      {/* Live Demo Section */}
      <section className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold mb-8 text-center">
            See It In Action
          </h2>
          <TypingDemo
            text="typesim simulates realistic human typing with natural pauses, typos, and corrections. Perfect for demos and presentations!"
            speed={30}
          />
        </div>
      </section>

      {/* Features Grid */}
      <section className="container mx-auto px-4 py-16 bg-muted/50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold mb-12 text-center">
            Features
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <FeatureCard
              title="Realistic Typos"
              description="Randomly hits neighboring keys on QWERTY keyboard and automatically corrects them naturally."
              icon={<Keyboard />}
            />
            <FeatureCard
              title="Variable Speed"
              description="Randomized delays between keystrokes with longer pauses at sentence boundaries and commas."
              icon={<Zap />}
            />
            <FeatureCard
              title="Mid-Sentence Edits"
              description="Goes back to change words, insert phrases, or improve text mid-typing for authentic behavior."
              icon={<FileText />}
            />
            <FeatureCard
              title="AI-Powered"
              description="Optional Gemini API integration for smarter word suggestions and sentence rephrasing."
              icon={<Brain />}
            />
            <FeatureCard
              title="Keyboard Shortcuts"
              description="Pause, speed control, and emergency stop with intuitive keyboard shortcuts during typing."
              icon={<Settings />}
            />
            <FeatureCard
              title="File Loading"
              description="Load text from files or paste directly. Supports multiline text with proper formatting."
              icon={<FileText />}
            />
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold mb-12 text-center">
            How It Works
          </h2>
          <div className="space-y-12">
            <div className="neo-card">
              <div className="flex items-start gap-4">
                <div className="neo-border bg-primary text-primary-foreground w-12 h-12 flex items-center justify-center font-bold text-xl shrink-0">
                  1
                </div>
                <div>
                  <h3 className="text-2xl font-bold mb-2">Install</h3>
                  <p className="text-muted-foreground mb-4">
                    Install typesim using UV, the modern Python package manager.
                  </p>
                  <Terminal command="uv tool install git+https://github.com/pc-style/typesim.git" />
                </div>
              </div>
            </div>

            <div className="neo-card">
              <div className="flex items-start gap-4">
                <div className="neo-border bg-primary text-primary-foreground w-12 h-12 flex items-center justify-center font-bold text-xl shrink-0">
                  2
                </div>
                <div>
                  <h3 className="text-2xl font-bold mb-2">Configure</h3>
                  <p className="text-muted-foreground mb-4">
                    Customize typing behavior through the TUI settings menu.
                    Adjust typo probability, speed, pauses, and AI features.
                  </p>
                  <CodeBlock
                    code={`# Settings are saved to ~/.typesim/config.yaml
# Configure:
# - Typo probability (0-50%)
# - Edit probability (0-100%)
# - Typing speed ranges
# - Thinking pauses
# - AI integration toggle`}
                    language="yaml"
                  />
                </div>
              </div>
            </div>

            <div className="neo-card">
              <div className="flex items-start gap-4">
                <div className="neo-border bg-primary text-primary-foreground w-12 h-12 flex items-center justify-center font-bold text-xl shrink-0">
                  3
                </div>
                <div>
                  <h3 className="text-2xl font-bold mb-2">Type</h3>
                  <p className="text-muted-foreground mb-4">
                    Run typesim, enter your text, and watch it type naturally
                    into any application.
                  </p>
                  <Terminal
                    command="typesim"
                    output="Choose option from main menu:
1. Start Typing
2. Settings
3. Load from File

Enter text and switch to target app during countdown!"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto text-center neo-card bg-primary text-primary-foreground">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Ready to Get Started?
          </h2>
          <p className="text-lg mb-8 opacity-90">
            Install typesim and start simulating realistic typing behavior
            today.
          </p>
          <Link href="/docs">
            <Button
              size="lg"
              variant="secondary"
              className="neo-border-thick text-lg px-8 py-6"
            >
              Read the Docs
            </Button>
          </Link>
        </div>
      </section>

      <Footer />
    </div>
  );
}
