import type * as React from 'react';

/** La targa-logo, disegnata in CSS con i font del sistema. */
export interface TargaProps { size?: 'l' | 'm' | 's'; variante?: 'ghisa' | 'ottone'; dettagli?: boolean; anno?: string; matricola?: string; className?: string }
export declare function Targa(props: TargaProps): React.ReactElement;

/** Il plettro-medaglietta: icona, avatar, firma. */
export interface PlettroProps { size?: number; colore?: 'giallo' | 'ghisa'; sigla?: boolean; foro?: string; label?: string; className?: string }
export declare function Plettro(props: PlettroProps): React.ReactElement;

/** Timbro del collaudo, per gli audit. */
export interface TimbroProps { tipo?: 'fuori-norma' | 'da-rifare' | 'da-tenere' | 'collaudato'; inclinazione?: number; children?: React.ReactNode; className?: string }
export declare function Timbro(props: TimbroProps): React.ReactElement;

export interface BottoneProps { variante?: 'primario' | 'secondario' | 'su-scuro'; href?: string; target?: string; type?: 'button' | 'submit'; onClick?: () => void; children?: React.ReactNode; className?: string }
export declare function Bottone(props: BottoneProps): React.ReactElement;

export interface Capitolo { testo: string; href?: string; attivo?: boolean }
/** Apertura della proposta, su ghisa, con la fascia a strisce. */
export interface HeroProps { cliente?: string; logoCliente?: string; occhiello?: string; titolo: React.ReactNode; evidenza?: string; sottotitolo?: React.ReactNode; capitoli?: Array<string | Capitolo>; evidenziaUltimo?: boolean; ampersand?: boolean; className?: string }
export declare function Hero(props: HeroProps): React.ReactElement;

export interface SezioneProps { id?: string; occhiello?: string; titolo?: React.ReactNode; intro?: React.ReactNode; tono?: 'chiaro' | 'acciaio'; children?: React.ReactNode; className?: string }
export declare function Sezione(props: SezioneProps): React.ReactElement;

export interface CartaAuditProps { timbro?: TimbroProps['tipo']; titolo: React.ReactNode; testo: React.ReactNode; direzione?: React.ReactNode; children?: React.ReactNode; className?: string }
export declare function CartaAudit(props: CartaAuditProps): React.ReactElement;

export interface ConsiglioProps { occhiello?: string; titolo?: React.ReactNode; firma?: string | null; children?: React.ReactNode; className?: string }
export declare function Consiglio(props: ConsiglioProps): React.ReactElement;

export interface Fase { titolo: string; testo: string; quando?: string }
export interface FasiProps { fasi?: Fase[]; className?: string }
export declare function Fasi(props: FasiProps): React.ReactElement;

export interface RigaInvestimento { voce: string; descrizione: React.ReactNode; prezzo: string; mercato?: string; extra?: boolean }
export interface InvestimentoProps { righe: RigaInvestimento[]; totale?: { voce?: string; descrizione?: string; prezzo: string; mercato?: string }; etichettaPrezzo?: string; impegno?: { titolo?: string; testo?: string } | null; nota?: string; className?: string }
export declare function Investimento(props: InvestimentoProps): React.ReactElement;

export interface Persona { nome: string; ruolo: string; foto?: string; testo?: string; competenze?: string[] }
export interface ChiSiamoProps { persone: Persona[]; className?: string }
export declare function ChiSiamo(props: ChiSiamoProps): React.ReactElement;

export interface BriefProps { occhiello?: string; titolo?: string; testo?: string; domande?: string[]; href: string; cta?: string; tempi?: string; className?: string }
export declare function Brief(props: BriefProps): React.ReactElement;

export interface PiePaginaProps { email?: string; validita?: string; nota?: string; className?: string }
export declare function PiePagina(props: PiePaginaProps): React.ReactElement;

declare global { interface Window { RockRoll: { Targa: typeof Targa; Plettro: typeof Plettro; Timbro: typeof Timbro; Bottone: typeof Bottone; Hero: typeof Hero; Sezione: typeof Sezione; CartaAudit: typeof CartaAudit; Consiglio: typeof Consiglio; Fasi: typeof Fasi; Investimento: typeof Investimento; ChiSiamo: typeof ChiSiamo; Brief: typeof Brief; PiePagina: typeof PiePagina } } }
