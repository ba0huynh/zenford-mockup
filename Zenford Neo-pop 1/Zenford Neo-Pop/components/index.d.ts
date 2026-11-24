/** Zenford Neo-Pop. Components are CSS classes (prefix zf-) plus small helpers on window.ZenfordNP. */
export type ZenState = "normal"|"happy"|"wow"|"wink"|"think"|"love"|"sad"|"fierce";
export type ZenOutfit = ""|"cape"|"phones"|"tv"|"pencil"|"mic"|"book"|"helmet";
/** Returns the Zen mascot as an SVG string. hood = shirt colour token value (default sky). */
export declare function zenSVG(state?: ZenState, hood?: string, outfit?: ZenOutfit, label?: string): string;
/** Changes the expression of a Zen already on the page. */
export declare function setZen(host: Element, state: ZenState): void;
/** The bubble-Z mark as an SVG string. fill: cobalt (default ground), yellow (on ink), white (on pastel). */
export declare function logoSVG(fill: string, size: number): string;
/** Fills every [data-zen="state|hood|outfit"] and [data-logo="#fill"] inside root. Outfit "follow" makes the eyes track the pointer. */
export declare function mount(root?: ParentNode): void;
export declare function followEyes(): void;
export declare function blink(): void;
export interface ButtonProps { variant?: "primary"|"white"|"dark"; size?: "md"|"sm"; disabled?: boolean; children: string }
export interface CardProps { hover?: boolean; tilt?: "l"|"r"; background?: "paper"|"mint"|"lavender"|"peach"|"sky"|"butter"|"yellow" }
export interface OverlineProps { children: string }
export interface TagProps { tone?: "default"|"ok"|"warn"|"note"|"ink"; children: string }
export interface PillProps { pressed: boolean; children: string }
export interface SwitchProps { checked: boolean; label: string }
export interface ProgressBarProps { value: number; tone?: "ink"|"yellow" }
export interface AnswerOptionProps { state?: "idle"|"ok"|"no"; children: string }
export interface LangTileProps { glyph: string; code: string; name: string; background: string }
export interface ZenSayProps { state: ZenState; outfit?: ZenOutfit; children: string }
