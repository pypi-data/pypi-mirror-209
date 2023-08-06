multipronto will be a package that contains an implementation of the PRONTO 
protocol.  PRONTO is a lightweight protocol for multiplexing several streams 
across a single stream.  I.e., running commands on a remote server, while
also copying files, without opening multiple TCP streams.

Planned feature list:
 - Pure Python implementation that requires no installation
   * Included dropper finds or loads the shell onto the remote machine
 - Thread-safe
   * Convenience wrappers provided to connect streams to file descriptors.
 - Symmetric
   * There is no client or host
 - Untrusted
   * Neither partner must trust the other to interact.
   * (If one peer runs a shell, it must trust the client.)
