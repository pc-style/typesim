import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { FeatureCard } from '@/components/feature-card';
import { TypingDemo } from '@/components/typing-demo';
import { CodeBlock } from '@/components/code-block';
import { Terminal } from '@/components/terminal';
import { Footer } from '@/components/footer';
import { Github, Zap, Brain, Keyboard, FileText, Settings, ShieldCheck, Terminal as TerminalIcon, Clock, Edit3 } from 'lucide-react';

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-b from-background via-primary/5 to-background">
      {/* Navigation */}
      <nav className="border-b bg-background/80 sticky top-0 z-50 backdrop-blur-md">
        <div className="container mx-auto px-4 py-5 flex items-center justify-between">
          <Link href="/" className="font-bold text-2xl tracking-tight hover:text-primary transition-colors">
            typesim
          </Link>
          <div className="flex items-center gap-3">
            <Link href="/docs">
              <Button variant="ghost" className="font-semibold">Documentation</Button>
            </Link>
            <a
              href="https://github.com/pc-style/typesim"
              target="_blank"
              rel="noopener noreferrer"
            >
              <Button variant="outline" className="font-semibold">
                <Github className="w-4 h-4 mr-2" />
                GitHub
              </Button>
            </a>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="container mx-auto px-4 py-32 md:py-48">
        <div className="max-w-5xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 mb-8 px-4 py-2 rounded-full border bg-primary/5 text-primary font-medium text-sm">
            <ShieldCheck className="w-4 h-4" />
            Bypass Typing Analysis Systems
          </div>
          <h1 className="text-5xl md:text-7xl font-bold mb-6 leading-tight tracking-tight">
            Realistic Typing
            <br />
            <span className="bg-gradient-to-r from-primary to-primary/60 bg-clip-text text-transparent">Simulator</span>
          </h1>
          <p className="text-lg md:text-xl text-muted-foreground mb-12 max-w-2xl mx-auto leading-relaxed">
            AI-powered Python tool that simulates authentic human typing patterns with typos, corrections, and natural pauses. 
            Designed to bypass typing analysis systems like GPTZero. Use responsibly.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-20">
            <Link href="/docs">
              <Button size="lg" className="text-base px-8 h-12 font-semibold">
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
                className="text-base px-8 h-12 font-semibold"
              >
                <Github className="w-5 h-5 mr-2" />
                View on GitHub
              </Button>
            </a>
          </div>
          
          {/* Quick stats */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 max-w-3xl mx-auto">
            <div className="rounded-xl border bg-card/50 backdrop-blur p-6 shadow-lg hover:shadow-xl hover:shadow-primary/20 transition-all hover:-translate-y-1">
              <div className="text-2xl font-bold text-primary mb-1">100%</div>
              <div className="text-sm text-muted-foreground">Human-like Behavior</div>
            </div>
            <div className="rounded-xl border bg-card/50 backdrop-blur p-6 shadow-lg hover:shadow-xl hover:shadow-primary/20 transition-all hover:-translate-y-1">
              <div className="text-2xl font-bold text-primary mb-1">AI-Powered</div>
              <div className="text-sm text-muted-foreground">Smart Suggestions</div>
            </div>
            <div className="rounded-xl border bg-card/50 backdrop-blur p-6 shadow-lg hover:shadow-xl hover:shadow-primary/20 transition-all hover:-translate-y-1">
              <div className="text-2xl font-bold text-primary mb-1">Open Source</div>
              <div className="text-sm text-muted-foreground">MIT Licensed</div>
            </div>
          </div>
        </div>
      </section>

      {/* Live Demo Section */}
      <section className="container mx-auto px-4 py-24">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold mb-3 tracking-tight">
              See It In Action
            </h2>
            <p className="text-base text-muted-foreground">
              Watch how typesim creates authentic human typing patterns
            </p>
          </div>
          <Terminal
            command="typesim"
            output={`  typesim
  ───────

  made by pcstyle

[?] :

 > Start Typing
   Settings
   Presets
   Load from File
   Export Config
   Import Config
   Reset to Defaults
   Quit`}
          />
        </div>
      </section>

      {/* Features Grid */}
      <section className="container mx-auto px-4 py-24">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-3 tracking-tight">
              Powerful Features
            </h2>
            <p className="text-base text-muted-foreground max-w-2xl mx-auto">
              Everything you need to simulate authentic human typing behavior
            </p>
          </div>
          
          {/* Primary Feature - Detection Bypass */}
          <div className="rounded-xl border bg-gradient-to-br from-primary/10 to-primary/5 mb-8 p-8 shadow-lg shadow-primary/10">
            <div className="flex items-start gap-6">
              <div className="rounded-lg bg-primary/20 text-primary p-3 shrink-0 shadow-md">
                <ShieldCheck className="w-6 h-6" />
              </div>
              <div>
                <h3 className="text-xl font-semibold mb-2 text-primary">Bypass Typing Analysis Systems</h3>
                <p className="text-base text-muted-foreground leading-relaxed">
                  Designed specifically to evade typing-process detectors like GPTZero typing analysis. 
                  Simulates authentic human timing patterns, natural edits, and realistic corrections 
                  to minimize detection signals. Perfect for maintaining privacy in your typing behavior.
                </p>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <FeatureCard
              title="Realistic Typos"
              description="Randomly hits neighboring keys on QWERTY keyboard and automatically corrects them naturally, just like a real human would."
              icon={<Keyboard className="w-6 h-6" />}
            />
            <FeatureCard
              title="Variable Speed"
              description="Randomized delays between keystrokes with longer pauses at sentence boundaries and commas for authentic rhythm."
              icon={<Clock className="w-6 h-6" />}
            />
            <FeatureCard
              title="Mid-Sentence Edits"
              description="Goes back to change words, insert phrases, or improve text mid-typing for genuine human behavior patterns."
              icon={<Edit3 className="w-6 h-6" />}
            />
            <FeatureCard
              title="AI-Powered"
              description="Optional Gemini API integration for intelligent word suggestions and natural sentence rephrasing capabilities."
              icon={<Brain className="w-6 h-6" />}
            />
            <FeatureCard
              title="Keyboard Shortcuts"
              description="Pause, speed control, and emergency stop with intuitive keyboard shortcuts during active typing sessions."
              icon={<Settings className="w-6 h-6" />}
            />
            <FeatureCard
              title="File Loading"
              description="Load text from files or paste directly. Supports multiline text with proper formatting and structure."
              icon={<FileText className="w-6 h-6" />}
            />
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="container mx-auto px-4 py-24">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-3 tracking-tight">
              How It Works
            </h2>
            <p className="text-base text-muted-foreground">
              Get started in three simple steps
            </p>
          </div>
          <div className="space-y-6">
            <div className="rounded-xl border bg-card p-6 hover:border-primary/50 transition-all shadow-md hover:shadow-lg hover:shadow-primary/10">
              <div className="flex items-start gap-6">
                <div className="rounded-lg bg-gradient-to-br from-primary to-primary/80 text-primary-foreground w-12 h-12 flex items-center justify-center font-semibold text-lg shrink-0 shadow-md">
                  1
                </div>
                <div className="flex-1">
                  <h3 className="text-xl font-semibold mb-2">Install</h3>
                  <p className="text-muted-foreground mb-4 text-sm">
                    Install typesim using UV, the modern Python package manager. Quick and easy setup.
                  </p>
                  <Terminal command="uv tool install git+https://github.com/pc-style/typesim.git" />
                </div>
              </div>
            </div>

            <div className="rounded-xl border bg-card p-6 hover:border-primary/50 transition-all shadow-md hover:shadow-lg hover:shadow-primary/10">
              <div className="flex items-start gap-6">
                <div className="rounded-lg bg-gradient-to-br from-primary to-primary/80 text-primary-foreground w-12 h-12 flex items-center justify-center font-semibold text-lg shrink-0 shadow-md">
                  2
                </div>
                <div className="flex-1">
                  <h3 className="text-xl font-semibold mb-2">Configure</h3>
                  <p className="text-muted-foreground mb-4 text-sm">
                    Customize typing behavior through the intuitive TUI settings menu.
                    Fine-tune every aspect of the simulation.
                  </p>
                  <Terminal
                    command="typesim"
                    output={`  settings
  ────────

  typo probability            8.0%
  edit probability           18.0%
  rephrase probability       30.0%

  base delay                 30-150ms
  thinking pause             500-2000ms
  sentence pause             800-2500ms
  comma pause                200-600ms

  use ai                     yes
  countdown                  3s
  speed                      1.0x

[?] :

 > Typo Probability
   Edit Probability
   Rephrase Probability
   Base Delay
   Toggle AI
   Back`}
                  />
                </div>
              </div>
            </div>

            <div className="rounded-xl border bg-card p-6 hover:border-primary/50 transition-all shadow-md hover:shadow-lg hover:shadow-primary/10">
              <div className="flex items-start gap-6">
                <div className="rounded-lg bg-gradient-to-br from-primary to-primary/80 text-primary-foreground w-12 h-12 flex items-center justify-center font-semibold text-lg shrink-0 shadow-md">
                  3
                </div>
                <div className="flex-1">
                  <h3 className="text-xl font-semibold mb-2">Type</h3>
                  <p className="text-muted-foreground mb-4 text-sm">
                    Run typesim, enter your text, and watch it type naturally into any application.
                  </p>
                  <Terminal
                    command="typesim"
                    output={`  typesim
  ───────

  made by pcstyle

[?] : > Start Typing

[?] Enter your text (press Enter twice to finish):

  Switch to your target app in 3 seconds...
  2...
  1...
  
  Typing... (Press Space to pause, Esc to stop)`}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="container mx-auto px-4 py-24">
        <div className="max-w-4xl mx-auto text-center rounded-xl border bg-gradient-to-br from-primary to-primary/80 text-primary-foreground p-12 shadow-2xl shadow-primary/30">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">
            Ready to Get Started?
          </h2>
          <p className="text-xl mb-10 opacity-95 leading-relaxed max-w-2xl mx-auto">
            Install typesim and start simulating authentic human typing behavior.
            Bypass detection systems with ease.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/docs">
              <Button
                size="lg"
                variant="secondary"
                className="text-lg px-10 py-7 font-bold shadow-lg hover:shadow-xl transition-shadow"
              >
                Read the Docs
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
                className="text-lg px-10 py-7 font-bold bg-primary-foreground text-primary shadow-lg hover:shadow-xl transition-shadow"
              >
                <Github className="w-5 h-5 mr-2" />
                Star on GitHub
              </Button>
            </a>
          </div>
        </div>
      </section>

      <Footer />
    </div>
  );
}
