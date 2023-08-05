# Change log:

## Version 0.1.1.7

### Added
    - Messages now have a method called .get_timestamp(). It returns None if the message does not have a header yet.

### Changed
    - Extract messages that have categories to different files, but re-exports them in the messages.py file.
    
### Fixed

### Version 0.1.1.5
    - Fix .block_outgoing() bug

## Version 0.1.1.6

### Added
    
### Changed
    - Delay message deserialization
        - Now messages are deserialized only when passed to functions by the subscriber, so they are kept as bytes as long as possible.
    - Better error message when deserializing unknown inlined message
    - Cleaner example
    
### Fixed
    - Fix unknown_message
        - Remove unnecessary attributes