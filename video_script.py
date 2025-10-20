from manim import *
import numpy as np

class BusinessProtectionVideo(Scene):
    def construct(self):
        # SCENE 1 - THE DREAM
        title = Text("The Retirement Trap", font_size=72, color=WHITE)
        subtitle = Text("Why Your Business Might Not Fund Your Retirement", font_size=36, color=RED)
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        
        # Business owner icons
        john = Circle(radius=0.5, color=BLUE, fill_opacity=0.8)
        john_label = Text("John", font_size=20).next_to(john, DOWN)
        mary = Circle(radius=0.5, color=PINK, fill_opacity=0.8)
        mary_label = Text("Mary", font_size=20).next_to(mary, DOWN)
        mary.next_to(john, RIGHT, buff=1)
        
        dream_text = Text("Dream: $3M Sale → Comfortable Retirement", font_size=30, color=GREEN)
        dream_text.next_to(mary, RIGHT, buff=1)
        
        self.play(FadeIn(john), FadeIn(mary), Write(john_label), Write(mary_label))
        self.play(Write(dream_text))
        self.wait(2)

        # SCENE 2 - THE REALITY
        self.play(FadeOut(title), FadeOut(subtitle))
        
        stat_text = Text("80% of Small Businesses", font_size=48, color=WHITE)
        dont_sell = Text("DON'T SELL", font_size=72, color=RED)
        stat_text.to_edge(UP)
        dont_sell.next_to(stat_text, DOWN)
        
        self.play(Write(stat_text))
        self.play(Write(dont_sell))
        self.wait(1)
        
        # Asset vs Stock sale explanation
        asset_sale = Text("Asset Sale = Higher Taxes + Lower Price", font_size=30, color=RED)
        stock_sale = Text("Stock Sale = Lower Taxes + Higher Price", font_size=30, color=GREEN)
        asset_sale.shift(UP * 0.5)
        stock_sale.shift(DOWN * 0.5)
        
        self.play(Write(asset_sale))
        self.play(Write(stock_sale))
        self.wait(2)

        # SCENE 3 - THE MATH BREAKDOWN
        self.clear()
        
        math_title = Text("The Retirement Math", font_size=48, color=WHITE)
        math_title.to_edge(UP)
        self.play(Write(math_title))
        
        # 401k calculation
        savings_data = VGroup(
            Text("401k after 30 years:", font_size=28),
            Text("$2,800,000", font_size=36, color=GREEN),
            Text("Roth IRA:", font_size=28),
            Text("$500,000", font_size=36, color=BLUE),
            Text("Social Security:", font_size=28),
            Text("$55,000/year", font_size=36, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(LEFT * 3)
        
        self.play(Write(savings_data))
        self.wait(1)
        
        # Income summary
        income_group = VGroup(
            Text("Total Retirement Income:", font_size=28),
            Text("$187,000/year", font_size=42, color=GREEN),
            Text("John's Current Income:", font_size=28),
            Text("$650,000/year", font_size=42, color=RED),
            Text("ANNUAL INCOME GAP:", font_size=32),
            Text("$463,000", font_size=48, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(RIGHT * 3)
        
        self.play(Write(income_group))
        self.wait(2)

        # SCENE 4 - THE SOLUTION
        self.clear()
        
        solution_title = Text("The Business Value Protection Plan", font_size=48, color=GREEN)
        solution_title.to_edge(UP)
        
        plan_details = VGroup(
            Text("• Started 18 years ago", font_size=30),
            Text("• $50K/year for 15 years", font_size=30),
            Text("• Now worth: $1,200,000", font_size=30, color=GREEN),
            Text("• Provides tax-free income", font_size=30, color=BLUE)
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP * 0.5)
        
        self.play(Write(solution_title))
        self.play(Write(plan_details))
        self.wait(2)

        # SCENE 5 - THE COMPARISON
        self.clear()
        
        comp_title = Text("With vs Without Protection Plan", font_size=42, color=WHITE)
        comp_title.to_edge(UP)
        
        # Without plan
        without_group = VGroup(
            Text("WITHOUT PLAN:", font_size=32, color=RED),
            Text("Business Income: $69,036", font_size=24),
            Text("Savings Income: $187,000", font_size=24),
            Text("TOTAL: $256,036/year", font_size=28, color=RED),
            Text("GAP: $393,964", font_size=32, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # With plan
        with_group = VGroup(
            Text("WITH PROTECTION PLAN:", font_size=32, color=GREEN),
            Text("Business Income: $69,036", font_size=24),
            Text("Savings Income: $187,000", font_size=24),
            Text("Plan Income: $48,000", font_size=24, color=GREEN),
            Text("TOTAL: $304,036/year", font_size=28, color=GREEN),
            Text("GAP: $345,964", font_size=32, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        without_group.shift(LEFT * 3.5)
        with_group.shift(RIGHT * 3.5)
        
        self.play(Write(comp_title))
        self.play(Write(without_group))
        self.play(Write(with_group))
        
        # Highlight the difference
        difference = Text("+$48,000 TAX-FREE INCOME!", font_size=36, color=GREEN)
        difference.shift(DOWN * 2)
        
        self.play(Write(difference))
        self.wait(2)

        # SCENE 6 - CALL TO ACTION
        self.clear()
        
        questions = VGroup(
            Text("What's your business really worth?", font_size=36, color=WHITE),
            Text("Could you survive on 50% less income?", font_size=36, color=RED),
            Text("What's your backup plan?", font_size=36, color=YELLOW)
        ).arrange(DOWN, buff=0.8)
        
        cta = Text("Protect your life's work before it's too late.", font_size=42, color=GREEN)
        cta.shift(DOWN * 2)
        
        self.play(Write(questions))
        self.wait(1)
        self.play(Write(cta))
        self.wait(3)
