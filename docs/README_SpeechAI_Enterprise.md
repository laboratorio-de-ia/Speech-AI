# Speech AI Pipeline

## Overview

Speech AI Pipeline is a modular Text-to-Speech platform designed with an
enterprise architecture.

## Features

-   Modular pipeline
-   Voice Profiles
-   Provider abstraction
-   Microsoft Edge TTS
-   Provider Factory / Registry
-   Configuration manager
-   Logging
-   Extensible architecture

## Architecture

``` text
Input Script
    |
Text Analyzer
    |
Presentation Model
    |
Narration Builder
    |
Speech Builder
    |
Speech Service
    |
Provider Factory
    |
Provider Registry
    |
Edge Provider
    |
MP3 Output
```

## Project Structure

    app/
    config/
    models/
    pipeline/
    providers/
    services/
    input/
    output/
    logs/
    tests/

## Pipeline

1.  Read script
2.  Analyze text
3.  Build presentation model
4.  Humanize narration
5.  Optimize speech
6.  Select voice profile
7.  Select provider
8.  Generate MP3

## Voice Profiles

Voice profiles are defined in `config/voices.json`.

## Providers

Current: - Edge TTS

Planned: - Azure Speech - OpenAI TTS - ElevenLabs - Amazon Polly

## Roadmap

-   Sprint 1--8: Core platform
-   Sprint 9: Dependency Injection & Plugin System
-   Sprint 10+: Multi-provider, Web UI, Packaging

## License

Copyright © Rodrigo Magalhães.
